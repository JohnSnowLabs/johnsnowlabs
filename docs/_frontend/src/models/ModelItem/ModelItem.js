import React from 'react';
import ModelItemTag from '../ModelItemTag';
import Tooltip from '../Tooltip';
import { addNamingConventions } from './utils';
import './ModelItem.css';

const MARKETPLACES = [
  { key: 'aws', label: 'AWS', icon: 'icon_aws.svg' },
  { key: 'azure', label: 'Azure', icon: 'icon_azure.svg' },
  { key: 'databricks', label: 'Databricks', icon: 'icon_databricks.svg' },
  { key: 'snowflake', label: 'Snowflake', icon: 'active_snowflake.svg' },
];

const MarketplaceIcon = ({ label, icon, deployLink }) => (
  <Tooltip label={label} compact>
    <a target="_blank" rel="noopener noreferrer" href={deployLink}>
      <figure><img src={`/assets/images/posts_image/${icon}`} alt={label} /></figure>
    </a>
  </Tooltip>
)

const ModelItemMarketplace = (marketplace) => {
  const available = MARKETPLACES.filter(({ key }) => marketplace[key]);
  if (available.length === 0) {
    return null;
  }
  return (
    <div className="model-item__footer">
      {available.map(({ key, label, icon }) => (
        <MarketplaceIcon key={key} label={label} icon={icon} deployLink={marketplace[key]} />
      ))}
    </div>
  );
}

const ModelItem = ({
  title,
  url,
  task,
  language,
  edition,
  date,
  supported,
  recommended,
  deprecated,
  highlight,
  marketplace,
}) => {
  let body;
  if (highlight && highlight.body && highlight.body[0]) {
    body = highlight.body[0];
  }

  const getDisplayedDate = () => {
    const [year, month] = date.split('-');
    return month + '.' + year;
  };

  let label;
  if (deprecated) {
    label = <div className="model-item__deprecated">Deprecated</div>;
  } else if (supported) {
    label = <div className="model-item__supported">Supported</div>;
  }

  return (
    <div className="cell cell--12 cell--md-6 cell--lg-4">
      <div className="model-item">
        {label}
        {recommended && (
          <span className="fa fa-star model-item__recommended"></span>
        )}
        <div className="model-item__header">
          <a href={url} className="model-item__title">
            {addNamingConventions(title)}
          </a>
        </div>
        <div className="model-item__content">
          {body && (
            <div
              className="model-item__highlight"
              dangerouslySetInnerHTML={{ __html: body }}
            />
          )}
          <ModelItemTag
            icon="calendar-alt"
            name="Date"
            value={getDisplayedDate()}
          />
          <ModelItemTag
            icon="edit"
            name="task"
            value={Array.isArray(task) ? task.join(', ') : task}
          />
          <ModelItemTag icon="flag" name="Language" value={language} />
          <ModelItemTag icon="clone" name="Edition" value={edition} />
        </div>

        {marketplace && <ModelItemMarketplace {...marketplace} />}
      </div>
    </div>
  );
};

export default ModelItem;
